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
    namaPekerjaan = db.Column(db.TEXT, primary_key=True)
    nomorKontrak = db.Column(db.String(100))
    nominalKontrak = db.Column(db.Integer)
    vendor = db.Column(db.String(100))
    status = db.Column(db.String(100))
    updated = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class ModelProgressPekerjaan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    n_spjl_begih = db.Column(db.Integer)
    n_spkpj_begih = db.Column(db.Integer)
    n_spbl_begih = db.Column(db.Integer)
    n_spkpb_begih = db.Column(db.Integer)
    n_spjl_betrak = db.Column(db.Integer)
    n_spkpj_betrak = db.Column(db.Integer)
    n_spbl_betrak = db.Column(db.Integer)
    n_spkpb_betrak = db.Column(db.Integer)
    val_spjl_begih = db.Column(db.Float)
    val_spkpj_begih = db.Column(db.Float)
    val_spbl_begih = db.Column(db.Float)
    val_spkpb_begih = db.Column(db.Float)
    val_spjl_betrak = db.Column(db.Float)
    val_spkpj_betrak = db.Column(db.Float)
    val_spbl_betrak = db.Column(db.Float)
    val_spkpb_betrak = db.Column(db.Float)


db.create_all()
'''
http://localhost:5000/siap-bayar/api/v1/progress?n_spjl_begih=1&n_spkpj_begih=1&n_spbl_begih=1&n_spkpb_begih=1&n_spjl_betrak=1&n_spkpj_betrak=1&n_spbl_betrak=1&n_spkpb_betrak=1&val_spjl_begih=1&val_spkpj_begih=1&val_spbl_begih=1&val_spkpb_begih=1&val_spjl_betrak=1&val_spkpj_betrak=1&val_spbl_betrak=1&val_spkpb_betrak=1
'''


class GetAllProgressData(Resource):
    def get(self):
        try:
            query = ModelProgressPekerjaan.query.all()[0]
            response = {
                "status": "success",
                "code": 200,
                "data": {
                    "n_spjl_begih": query.n_spjl_begih,
                    "n_spkpj_begih": query.n_spkpj_begih,
                    "n_spbl_begih": query.n_spbl_begih,
                    "n_spkpb_begih": query.n_spkpb_begih,
                    "n_spjl_betrak": query.n_spjl_betrak,
                    "n_spkpj_betrak": query.n_spkpj_betrak,
                    "n_spbl_betrak": query.n_spbl_betrak,
                    "n_spkpb_betrak": query.n_spkpb_betrak,
                    "val_spjl_begih": query.val_spjl_begih,
                    "val_spkpj_begih": query.val_spkpj_begih,
                    "val_spbl_begih": query.val_spbl_begih,
                    "val_spkpb_begih": query.val_spkpb_begih,
                    "val_spjl_betrak": query.val_spjl_betrak,
                    "val_spkpj_betrak": query.val_spkpj_betrak,
                    "val_spbl_betrak": query.val_spbl_betrak,
                    "val_spkpb_betrak": query.val_spkpb_betrak,
                    "n_begih": query.n_spjl_begih + query.n_spkpj_begih + query.n_spbl_begih + query.n_spkpb_begih,
                    "n_betrak": query.n_spjl_betrak + query.n_spkpj_betrak + query.n_spbl_betrak + query.n_spkpb_betrak,
                    "val_begih": query.val_spjl_begih + query.val_spkpj_begih + query.val_spbl_begih + query.val_spkpb_begih,
                    "val_betrak": query.val_spjl_betrak + query.val_spkpj_betrak + query.val_spbl_betrak + query.val_spkpb_betrak,
                }
            }
            return response, 200
        except:
            return {
                "status": "failed",
                "code": 404,
                "message": "No data available"
            }, 404

    def delete(self):
        query = ModelProgressPekerjaan.query.all()
        for data in query:
            db.session.delete(data)
            db.session.commit()
        return {
            "message": "All data removed",
            "status": "success",
            "code": 200
        }


class GetProgressData(Resource):
    def get(self):
        n_spjl_begih = request.args.get('n_spjl_begih')
        n_spkpj_begih = request.args.get('n_spkpj_begih')
        n_spbl_begih = request.args.get('n_spbl_begih')
        n_spkpb_begih = request.args.get('n_spkpb_begih')
        n_spjl_betrak = request.args.get('n_spjl_betrak')
        n_spkpj_betrak = request.args.get('n_spkpj_betrak')
        n_spbl_betrak = request.args.get('n_spbl_betrak')
        n_spkpb_betrak = request.args.get('n_spkpb_betrak')
        val_spjl_begih = request.args.get('val_spjl_begih')
        val_spkpj_begih = request.args.get('val_spkpj_begih')
        val_spbl_begih = request.args.get('val_spbl_begih')
        val_spkpb_begih = request.args.get('val_spkpb_begih')
        val_spjl_betrak = request.args.get('val_spjl_betrak')
        val_spkpj_betrak = request.args.get('val_spkpj_betrak')
        val_spbl_betrak = request.args.get('val_spbl_betrak')
        val_spkpb_betrak = request.args.get('val_spkpb_betrak')
        try:
            query = ModelProgressPekerjaan.query.all()[0]
            query.n_spjl_begih = request.args.get("n_spjl_begih")
            query.n_spkpj_begih = request.args.get("n_spkpj_begih")
            query.n_spbl_begih = request.args.get("n_spbl_begih")
            query.n_spkpb_begih = request.args.get("n_spkpb_begih")
            query.n_spjl_betrak = request.args.get("n_spjl_betrak")
            query.n_spkpj_betrak = request.args.get("n_spkpj_betrak")
            query.n_spbl_betrak = request.args.get("n_spbl_betrak")
            query.n_spkpb_betrak = request.args.get("n_spkpb_betrak")
            query.val_spjl_begih = request.args.get("val_spjl_begih")
            query.val_spkpj_begih = request.args.get("val_spkpj_begih")
            query.val_spbl_begih = request.args.get("val_spbl_begih")
            query.val_spkpb_begih = request.args.get("val_spkpb_begih")
            query.val_spjl_betrak = request.args.get("val_spjl_betrak")
            query.val_spkpj_betrak = request.args.get("val_spkpj_betrak")
            query.val_spbl_betrak = request.args.get("val_spbl_betrak")
            query.val_spkpb_betrak = request.args.get("val_spkpb_betrak")
            db.session.commit()
            response = {
                "status": "success",
                "code": 200,
                "data": {
                    "n_spjl_begih": query.n_spjl_begih,
                    "n_spkpj_begih": query.n_spkpj_begih,
                    "n_spbl_begih": query.n_spbl_begih,
                    "n_spkpb_begih": query.n_spkpb_begih,
                    "n_spjl_betrak": query.n_spjl_betrak,
                    "n_spkpj_betrak": query.n_spkpj_betrak,
                    "n_spbl_betrak": query.n_spbl_betrak,
                    "n_spkpb_betrak": query.n_spkpb_betrak,
                    "val_spjl_begih": query.val_spjl_begih,
                    "val_spkpj_begih": query.val_spkpj_begih,
                    "val_spbl_begih": query.val_spbl_begih,
                    "val_spkpb_begih": query.val_spkpb_begih,
                    "val_spjl_betrak": query.val_spjl_betrak,
                    "val_spkpj_betrak": query.val_spkpj_betrak,
                    "val_spbl_betrak": query.val_spbl_betrak,
                    "val_spkpb_betrak": query.val_spkpb_betrak,
                    "n_begih": query.n_spjl_begih + query.n_spkpj_begih + query.n_spbl_begih + query.n_spkpb_begih,
                    "n_betrak": query.n_spjl_betrak + query.n_spkpj_betrak + query.n_spbl_betrak + query.n_spkpb_betrak,
                    "val_begih": query.val_spjl_begih + query.val_spkpj_begih + query.val_spbl_begih + query.val_spkpb_begih,
                    "val_betrak": query.val_spjl_betrak + query.val_spkpj_betrak + query.val_spbl_betrak + query.val_spkpb_betrak,
                }

            }
            return response, 200
        except:
            data = ModelProgressPekerjaan(
                n_spjl_begih=n_spjl_begih,
                n_spkpj_begih=n_spkpj_begih,
                n_spbl_begih=n_spbl_begih,
                n_spkpb_begih=n_spkpb_begih,
                n_spjl_betrak=n_spjl_betrak,
                n_spkpj_betrak=n_spkpj_betrak,
                n_spbl_betrak=n_spbl_betrak,
                n_spkpb_betrak=n_spkpb_betrak,
                val_spjl_begih=val_spjl_begih,
                val_spkpj_begih=val_spkpj_begih,
                val_spbl_begih=val_spbl_begih,
                val_spkpb_begih=val_spkpb_begih,
                val_spjl_betrak=val_spjl_betrak,
                val_spkpj_betrak=val_spkpj_betrak,
                val_spbl_betrak=val_spbl_betrak,
                val_spkpb_betrak=val_spkpb_betrak
            )
            db.session.add(data)
            db.session.commit()
            response = {
                "message": "sukses input data",
                "status": "success",
                "code": 200
            }
            return response, 200


class GetAllData(Resource):
    def get(self):
        query = ModelPekerjaan.query.all()
        if query.__len__() != 0:
            data = {
                "status": "success",
                "code": 200,
                "data": [
                    {
                        "namapekerjaan": data.namaPekerjaan,
                        "nomorkontrak": data.nomorKontrak,
                        "nominalkontrak": data.nominalKontrak,
                        "vendor": data.vendor,
                        "status": data.status,
                        "update": str(data.updated)
                    }
                    for data in query
                ]}

            return data, 200
        else:
            return {
                "status": "failed",
                "code": 404,
                "message": "No data available "
            }, 404

    def delete(self):
        query = ModelPekerjaan.query.all()
        for data in query:
            db.session.delete(data)
            db.session.commit()
        return {
            "message": "All data removed",
            "status": "success",
            "code": 200
        }


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

        try:
            query = ModelPekerjaan.query.get(
                namaPekerjaan)
            if query.namaPekerjaan != namaPekerjaan:
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
                query.nomorKontrak = nomorKontrak
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
api.add_resource(
    GetProgressData, "/siap-bayar/api/v1/progress", methods=["GET"])
api.add_resource(GetAllProgressData,
                 "/siap-bayar/api/v1/progress/all", methods=["GET", "DELETE"])
if __name__ == "__main__":
    app.run(debug=True)
