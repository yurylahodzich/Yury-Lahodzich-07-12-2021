import axios from "axios";

export default axios.create({
  baseURL: "https://zymzom.tk/api/",
  headers: {
    "Content-type": "application/json"
  }
});
