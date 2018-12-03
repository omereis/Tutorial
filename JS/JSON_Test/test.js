var soj = {"sites":{"count":1,"site":[{"id":714303,"name":"Idan Cohen Gvaot","accountId":53508,"status":"Active","peakPower":7.47,"lastUpdateTime":"2018-11-14","installationDate":"2018-05-08","ptoDate":null,"notes":"","type":"Optimizers & Inverters","location":{"country":"Israel","city":"Giv'ot Bar","address":"Yakinton Street, Yakinton Street","address2":"","zip":"123456","timeZone":"Asia/Jerusalem","countryCode":"IL"},"primaryModule":{"manufacturerName":"Suntech","modelName":"STP325-24/vfm","maximumPower":325.0,"temperatureCoef":-0.8},"uris":{"DETAILS":"/site/714303/details","DATA_PERIOD":"/site/714303/dataPeriod","OVERVIEW":"/site/714303/overview"},"publicSettings":{"isPublic":false, "isPrivate":true}}]}};
soj = [{"thickness":0,"sld":2.069,"mu":0,"roughness":10},{"thickness":1250,"sld":4,"mu":0,"roughness":10},{"thickness":0,"sld":0,"mu":0,"roughness":0}];
//var soj = {"id":714303,"name":"Idan Cohen Gvaot","accountId":53508,"status":"Active","peakPower":7.47,"lastUpdateTime":"2018-11-14","installationDate":"2018-05-08","ptoDate":null,"notes":"","type":"Optimizers & Inverters"};
console.log("-----------------------------------------------------------------------");
console.log(JSON.stringify(soj));
console.log("-----------------------------------------------------------------------");
//-----------------------------------------------------------------------------
function count_keys (obj) {
    var count = 0, k;
    for (k in obj) {
        if (obj.hasOwnProperty(k))
            count++;
    }
    return (count);
}
//-----------------------------------------------------------------------------
function is_string (value) {
    var type = typeof (value);
    return (type == "string");
}
//-----------------------------------------------------------------------------
function get_bool_string (value) {
    var vResult;

    if (typeof(value) == "boolean")
        vResult = (value ? "true" : "false");
    else
        vResult = value;
    return (vResult);
}
//-----------------------------------------------------------------------------
function get_value_string(value) {
    var result = get_bool_string (value);
    if (result === null)
        result = "";
    return (result);
}
//-----------------------------------------------------------------------------
function print_json (objJson, strJSon, level=0) {
    var strLevel = ' '.repeat(level);
    for (var k in objJson) {
        strJSon += strLevel + k + ":";
        if (objJson.hasOwnProperty(k)) {
            var value = get_value_string(objJson[k]);
            var keys_count = Object.keys(value).length;
            if (is_string (value))
                keys_count = 0;
            if (keys_count > 0) {
                strJSon = print_json (value, strJSon + "\n", level + 1);
            }
            else {
                strJSon += value + "\n";
                console.log(strJSon);
            }
        }
    }
    return (strJSon);
}

var strJSon="";
strJSon = print_json (soj, strJSon);
strJSon = "Walla\n-----\n" + strJSon ;
console.log(strJSon);
