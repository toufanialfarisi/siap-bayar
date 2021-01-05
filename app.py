from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import datetime

basedir = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///" + os.path.join(basedir, "db.sqlite")

app = Flask(__name__)
api = Api(app)
CORS(app)

# SQLAlchemy
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Models


class ModelPekerjaan(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    namaPekerjaan = db.Column(db.TEXT)
    nomorKontrak = db.Column(db.String(100), primary_key=True)
    nominalKontrak = db.Column(db.Integer)
    vendor = db.Column(db.String(100))
    status = db.Column(db.String(100))
    updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)


db.create_all()


class GetAllData(Resource):
    def delete(self):
        query = ModelPekerjaan.query.all()
        for data in query:
            db.session.delete(data)
            db.session.commit()
        return {
            "message": "All data removed"
        }

    def get(self):
        query = ModelPekerjaan.query.all()
        data = [
            {
                "namapekerjaan": data.namaPekerjaan,
                "nomorkontrak": data.nomorKontrak,
                "nominalkontrak": data.nominalKontrak,
                "vendor": data.vendor,
                "status": data.status,
                "update": str(data.updated)
            }
            for data in query
        ]
        return data


class InserData(Resource):
    def get(self):
        namaPekerjaan = request.args.get("namapekerjaan")
        nomorKontrak = request.args.get("nomorkontrak")
        nominalKontrak = request.args.get("nominalkontrak")
        vendor = request.args.get("vendor")
        status = request.args.get("status")

        response_200 = {
            "message": "data berhasil dimasukan",
            "status": "success",
            "code": 200,
            "data": {
                "namapekerjaan": namaPekerjaan,
                "nomorkontrak": nomorKontrak,
                "nominalkontrak": nominalKontrak,
                "vendor": vendor,
                "status": status
            }
        }
        # data = ModelPekerjaan(
        #     namaPekerjaan=namaPekerjaan,
        #     nomorKontrak=nomorKontrak,
        #     nominalKontrak=nominalKontrak,
        #     vendor=vendor,
        #     status=status
        # )
        # db.session.add(data)
        # db.session.commit()
        # return response_200, 200

        try:
            query = ModelPekerjaan.query.get(
                nomorKontrak)
            if query.nomorKontrak != nomorKontrak:
                data = ModelPekerjaan(
                    namaPekerjaan=namaPekerjaan,
                    nomorKontrak=nomorKontrak,
                    nominalKontrak=nominalKontrak,
                    vendor=vendor,
                    status=status
                )
                db.session.add(data)
                db.session.commit()
                return response_200
            elif query.status != status:
                query.status = status
                db.session.commit()
                return {
                    "message": "data  diedit",
                    "status": "success",
                    "code": 200,
                    "data": {
                        "namapekerjaan": query.namaPekerjaan,
                        "nomorkontrak": query.nomorKontrak,
                        "nominalkontrak": query.nominalKontrak,
                        "vendor": query.vendor,
                        "status": query.status
                    }
                }, 200
            else:
                return {
                    "message": "duplicated data detected",
                    "status": "failed",
                    "code": 404
                }, 404

        except:
            data = ModelPekerjaan(
                namaPekerjaan=namaPekerjaan,
                nomorKontrak=nomorKontrak,
                nominalKontrak=nominalKontrak,
                vendor=vendor,
                status=status
            )
            db.session.add(data)
            db.session.commit()
            return response_200, 200


api.add_resource(GetAllData, "/siap-bayar/api/v1", methods=["GET", "DELETE"])
api.add_resource(InserData, "/siap-bayar/api/v1/data", methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True)
