class CarShowroom:
    def __init__(self):
        self.companies = {
            "Mercedes-Benz": {
                "models": {
                    "Mercedes-Benz EQA": {"variants": {"Base": 24000, "Premium": 28000}},
                    "Mercedes-Benz GCL": {"variants": {"Base": 18000, "Sport": 22000}}
                }
            },
            "Rolls": {
                "models": {
                    "GHost": {"variants": {"Standard": 20000, "Touring": 25000}},
                    "Accord": {"variants": {"LX": 23000, "EX": 27000}}
                }
            },
            "Ford": {
                "models": {
                    "Fiesta": {"variants": {"S": 15000, "SE": 17000}},
                    "Mustang": {"variants": {"EcoBoost": 27000, "GT": 35000}}
                }
            }
        }
        self.SGST = 0.08
        self.CGST = 0.08

    def select_car_company(self):
        while True:
            print("Available car companies: ", list(self.companies.keys()))
            company = input("Please enter the car company you want to select: ")
            if company in self.companies:
                return company
            else:
                print("Invalid car company. Please try again.")
    def select_car_model(self, company):
        while True:
            print(f"Available models for {company}: ", list(self.companies[company]["models"].keys()))
            model = input(f"Please enter the model you want to select from {company}: ")
            if model in self.companies[company]["models"]:
                return model
            else:
                print("Invalid model. Please try again.")
    def select_car_model(self, company):
        while True:
            print(f"Available models for {company}: ", list(self.companies[company]["models"].keys()))
            model = input(f"Please enter the model you want to select from {company}: ")
            if model in self.companies[company]["models"]:
                return model
            else:
                print("Invalid model. Please try again.")
    def select_car_variant(self, company, model):
        while True:
            print(f"Available variants for {model}: ", list(self.companies[company]["models"][model]["variants"].keys()))
            variant = input(f"Please enter the variant you want to select for {model}: ")
            if variant in self.companies[company]["models"][model]["variants"]:
                return variant
            else:
                print("Invalid variant. Please try again.")
    def calculate_price(self, company, model, variant):
        base_price = self.companies[company]["models"][model]["variants"][variant]
        sgst_amount = base_price * self.SGST
        cgst_amount = base_price * self.CGST
        total_price = base_price + sgst_amount + cgst_amount
        return base_price, sgst_amount, cgst_amount, total_price
    def run(self):
        company = self.select_car_company()
        model = self.select_car_model(company)
        variant = self.select_car_variant(company, model)
        base_price, sgst_amount, cgst_amount, total_price = self.calculate_price(company, model, variant)
        print(f"\nSelected Car Details:\nCompany: {company}\nModel: {model}\nVariant: {variant}")
        print(f"Base Price: RS{base_price}")
        print(f"SGST: Rs{sgst_amount}")
        print(f"CGST: Rs{cgst_amount}")
        print(f"Total Price: Rs{total_price}")
if __name__ == "__main__":
    c=CarShowroom()
    c.select_car_company()