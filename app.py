from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("customer_model.pkl")

# Business-friendly interpretation of the model's numeric classes.
# These names are based on the actual decision rules in customer_model.pkl.
SEGMENTS = {
    0: {
        "name": "Balanced Customer",
        "profile": "Mid Income · Moderate Spending",
        "description": "This customer shows a more balanced income and spending pattern.",
        "suggestion": "Use general offers, personalized recommendations, and engagement campaigns."
    },
    1: {
        "name": "High-Value Customer",
        "profile": "High Income · High Spending",
        "description": "This customer combines strong purchasing power with high spending activity.",
        "suggestion": "Focus on premium offers, loyalty benefits, and early access campaigns."
    },
    2: {
        "name": "Active Spender",
        "profile": "Lower Income · Higher Spending",
        "description": "This customer spends actively relative to their income level.",
        "suggestion": "Use value bundles, rewards, and targeted promotions to maintain engagement."
    },
    3: {
        "name": "Potential Premium Customer",
        "profile": "High Income · Low Spending",
        "description": "This customer has strong purchasing power but currently spends less.",
        "suggestion": "Use personalized premium recommendations and re-engagement offers."
    },
    4: {
        "name": "Low-Engagement Customer",
        "profile": "Lower Income · Lower Spending",
        "description": "This customer currently shows lower purchasing power and lower spending activity.",
        "suggestion": "Use affordable offers, discounts, and simple value-focused campaigns."
    }
}


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "success": True,
        "model": "Decision Tree",
        "features": ["Annual Income (k$)", "Spending Score (1-100)"]
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "Please send valid customer data."}), 400

        income = data.get("annual_income")
        spending = data.get("spending_score")

        if income is None or spending is None:
            return jsonify({
                "error": "Annual income and spending score are required."
            }), 400

        income = float(income)
        spending = float(spending)

        if not 15 <= income <= 137:
            return jsonify({
                "error": "Annual income must be between 15 and 137 k$."
            }), 400

        if not 1 <= spending <= 100:
            return jsonify({
                "error": "Spending score must be between 1 and 100."
            }), 400

        customer = pd.DataFrame([{
            "Annual Income (k$)": income,
            "Spending Score (1-100)": spending
        }])

        cluster = int(model.predict(customer)[0])
        segment = SEGMENTS.get(cluster, {
            "name": f"Customer Group {cluster}",
            "profile": "Customer segment",
            "description": "The model assigned this customer to this group.",
            "suggestion": "Review this segment before using it for business decisions."
        })

        return jsonify({
            "success": True,
            "customer": {
                "annual_income": income,
                "spending_score": spending
            },
            "prediction": {
                "cluster": cluster,
                **segment
            }
        })

    except (ValueError, TypeError):
        return jsonify({"error": "Please enter valid numerical values."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
