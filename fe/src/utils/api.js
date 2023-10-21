const post = (url, data, type) =>
  fetch(`/api${url}`, {
    method: "POST",
    headers: type ? {} : { "Content-Type": "application/json" },
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

export const apiGetStuCourse = (data) =>
  post("/user/query_homework_by_course", data);

export const apiSubmitStuCourse = (data) =>
  post("/user/submit_homework", data, "file");

// 老师拥有的课程
export const apiGetTeaCourse = (data) =>
  post("/user/query_course_by_teacher", data);

// 创建课程作业
export const apiNewWork = (data) => post("/user/create_course_homework", data);

// 返回这个课程所发布的所有作业
export const apiGetWork = (data) =>
  post("/user/query_homework_by_course", data);

// 删除作业
export const apiDelWork = (data) => post("/user/delete_homework", data);
