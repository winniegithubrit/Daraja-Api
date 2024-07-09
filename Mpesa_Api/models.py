from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class QRCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    MerchantName = db.Column(db.String(300), nullable=False)
    RefNo = db.Column(db.String(100))
    Amount = db.Column(db.String(100), nullable=False)
    TrxCode = db.Column(db.String(100), nullable=False)
    CPI = db.Column(db.String(100), nullable=False)
    Size = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "MerchantName": self.MerchantName,
            "RefNo": self.RefNo,
            "Amount": self.Amount,
            "TrxCode": self.TrxCode,
            "CPI": self.CPI,
            "Size": self.Size
        }
