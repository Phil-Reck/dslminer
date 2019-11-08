from flask import Flask
from flask import request
from . import timeseries
app = Flask(__name__)

# forecast indicator data
@app.route('/forecast/<indicatorid>/')
def show_user_profile(indicatorid):
    periodspan = request.args.get('periodspan') # the number of dependent values to be generated based on periodtype
    periodtype = request.args.get('periodtype') # can yealy 'Y' or montly 'M'
    ouid = request.args.get('ouid')  # orgunit id
    p=timeseries.predictor()
    app.logger.debug("===query parameters===")
    app.logger.debug(periodspan)
    app.logger.debug(periodtype)
    app.logger.debug(ouid)
    app.logger.debug("======")
    if(ouid==None):
        ouid=18 # National org unit id
    periodspan=int(periodspan)
    data=p.predict(indicatorid,ouid,periodtype,periodspan)

    # show the user profile for that user
    return data