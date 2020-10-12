import service from "../utils/request.js"


export function GetCates(){
    return service.request({
        method:"GET",
        url:"/nirs_cates"
    });
};