const API_URL = "http://127.0.0.1:8001";

export const getToken = () => localStorage.getItem("token");

export const apiRequest = async (endpoint, method = "POST", body) => {
  const token = getToken();

  const res = await fetch(`${API_URL}${endpoint}`, {
    method,
    headers: {
      "Content-Type": "application/json",
      Authorization: token ? `Bearer ${token}` : ""
    },
    body: body ? JSON.stringify(body) : undefined
  });

  return res.json();
};