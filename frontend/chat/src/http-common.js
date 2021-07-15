import axios from "axios";

export default axios.create({
  baseURL: "http://zymzom.tk/api/",
  headers: {
    "Content-type": "application/json"
  }
});
