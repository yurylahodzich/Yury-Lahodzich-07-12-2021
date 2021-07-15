import http from "../http-common";

class MessageDataService {

    create(data) {
        return http.post("/message/", data);
    }

    delete(id) {
        return http.delete(`/message/${id}/`);
    }

    findById(id) {
        return http.get(`/message/${id}/search_messages/`);
    }
}

export default new MessageDataService();