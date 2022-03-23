import http from "../http";

class ItemDataService {
    getAll() {
        return http.get("/items");
    }
    create(data) {//申请一个新的条目
        return http.post("/items", data);
    }
    update(id, data) {
        return http.put(`/items/${id}`, data);
    }
    delete(id) {
        return http.delete(`/items/${id}`);
    }
}
export default new ItemDataService();