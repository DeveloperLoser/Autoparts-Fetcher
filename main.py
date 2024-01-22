import requests
import vininfo

napa = 'https://www.napaonline.com/en/vehicle/add'
napa_api = 'https://accio.genpt.com/api/v1/core/'
api_headers = {
"site":"us"
"catalog_name":"ymm_en"
"request_id":"282iptx0m2v1702324940918"
"url":"https://www.napaonline.com/"
"ref_url":"https://www.napaonline.com/"
"request_type":"search"
"rows":"99"
"start":"0"
"_br_uid_2":"_br_uid_2_unavailable"
"fl":["item_id","year","year_id","year","year_id","make","make_id","model","model_id","application_ids","vehicle_type_id"]
"facet.field":""
"q":"*"
"efq":"vehicle_type:"Auto/Light Trucks" AND year:"2021" AND make:"Acura""
"search_type":"keyword"
"view_id":"base"
"f.model.facet.limit":"999"
}
vin = ''

def compose_payload(year,make,model):
    typeID = 1
    makeId = 
    return
    