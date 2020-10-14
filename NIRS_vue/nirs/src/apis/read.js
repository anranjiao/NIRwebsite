import service from "../utils/request.js"


export function GetCates(){
    return service.request({
        method:"GET",
        url:"/nirs_cates"
    });
};

export function GetInfoPost(postParams){
    return service.request({
        method:'post',
        url:postParams.url,
        data:{
            key:postParams.key,
            secretKey:'这是secretKey'//预留字段加密用
        }
    })
}