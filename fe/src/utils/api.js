const post = (url, data) =>
  fetch(`/api${url}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then((response) => {
      // network failure, request prevented
      if (response.status >= 200 && response.status < 300) {
        return Promise.resolve(response);
      }

      return Promise.reject(new Error(response.statusText));
    })
    .then((response) => response.json())
    .then((result) => {
      return Promise.resolve(result);
    })
    .catch((error) => {
      return Promise.resolve(error);
    });

export const apiLogin = (data) => post("/user/login", data);

export const apiReg = (data) => post("/user/register", data);
