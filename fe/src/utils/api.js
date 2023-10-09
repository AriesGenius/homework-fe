const post = (url, data, type) =>
  fetch(`/api${url}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: type ? data : JSON.stringify(data),
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

export const apiGetStuCourse = (data) => post("/user/query_homework", data);
export const apiSubmitStuCourse = (data) =>
  post("/user/submit_homework", data, "file");
