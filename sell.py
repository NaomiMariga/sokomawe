class Sell:
    def userSell(self, userId, itemImageLink,itemDescription, price, shippingFee, location, itemid):
        if itemImageLink:
            if itemDescription:
                if price:
                    if shippingFee:
                        if location:
                            sql = "INSERT INTO items"
                        else:
                            message = "Enter a valid location"
                    else:
                        message = "Provide the shipping fee"
                else:
                    message = "provide the Price"
            else:
                message = "item description must be provided"
        else:
            message = "image is missing"

        return {"success": True, "message": message}

