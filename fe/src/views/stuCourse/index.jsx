import React, { useEffect, useState } from "react";

import { Button, Form, Select, message, Upload, Input, Table } from "antd";

import { apiGetStuCourse, apiSubmitStuCourse } from "../../utils/api";

const user = JSON.parse(localStorage.getItem("user") || "{}");

export default function Index() {
  const [list, setList] = useState([]);

  const [fileList, setFileList] = useState([]);

  const submitFile = (param) => {
    console.log("param -> :", param);
    console.log("fileList -> :", fileList);

    const name = new FormData();

    fileList.forEach((file) => {
      name.append("file[]", file);
    });
    name.append("homework_name", param.homework_name);
    name.append("homework_course", param.homework_course);
    name.append("homework_user", param.homework_user);

    apiSubmitStuCourse(name).then((res) => {
      console.log("res -> :", res);
    });
  };

  const columns = [
    {
      title: "No.",
      dataIndex: "id",
      key: "id",
    },
    {
      title: "homework_name",
      dataIndex: "course_homework",
      key: "course_homework",
    },
    {
      title: "Course",
      dataIndex: "course_name",
      key: "course_name",
    },
    // {
    //   title: "Current Status",
    //   dataIndex: "submission_status",
    //   key: "submission_status",
    //   render: (text) => <>{stateObject[text]}</>,
    // },
    {
      title: "Date",
      dataIndex: "homework_time",
      key: "homework_time",
    },
    {
      title: "Operate",
      render: (row) => {
        return (
          <>
            <Upload
              showUploadList={false}
              name="file"
              action="/api/user/submit_homework"
              fileList={fileList}
              accept={".jpg, .jpeg, .png,.uxl"}
              onChange={(info) => {
                if (info.file.status !== "uploading") {
                  console.log(info.file, info.fileList);
                }
                if (info.file.status === "done") {
                  message.success(
                    `${info.file.name} file uploaded successfully`
                  );
                  getList();
                } else if (info.file.status === "error") {
                  message.error(`${info.file.name} file upload failed.`);
                }
              }}
              data={() => {
                return {
                  homework_name: row.course_homework,
                  homework_course: row.course_name,
                  homework_user: user.username,
                };
              }}
              beforeUpload={(file) => {
                if (
                  file.type !== "image/png" &&
                  file.type !== "image/jpeg" &&
                  file.type !== "image/jpg" &&
                  !file.name.includes(".uxl")
                ) {
                  message.error(`${file.name} must is png,jpg,uxl file`);
                  return false;
                }

                // setFileList([...fileList, file]);

                // const {
                //   course_homework: homework_name,
                //   course_name: homework_course,
                // } = row;

                // submitFile({
                //   homework_name,
                //   homework_course,
                //   homework_user: user.username,
                // });
              }}
            >
              <Button>Submiting</Button>
            </Upload>
            &nbsp; &nbsp;
            {row.submit && (
              <Button type="link" href={row.homework_content} target="_blank">
                Faceback
              </Button>
            )}
          </>
        );
      },
    },
  ];

  const stateMap = [
    { label: "submitted", value: "1" },
    { label: "uncommitted", value: "2" },
  ];

  const stateObject = stateMap.reduce((obj, item) => {
    obj[item.value] = item.label;
    return obj;
  }, {});

  const [form] = Form.useForm();

  const getList = () => {
    apiGetStuCourse({
      username: user.username,
      course_name: form.getFieldValue("course"),
    }).then((res) => {
      console.log("res -> :", res);
      setList(res.data?.courses || []);
    });
  };

  return (
    <>
      <Form layout="inline" form={form}>
        <Form.Item label="Course" name="course">
          <Input placeholder="Course Name" />
        </Form.Item>
        {/* <Form.Item label="submission status" name="submission_status">
          <Select style={{ width: "180px" }} placeholder="Submission Status">
            {stateMap.map((item) => (
              <Select.Option value={item.value} key={item.value}>
                {item.label}
              </Select.Option>
            ))}
          </Select>
        </Form.Item> */}
        <Form.Item>
          <Button type="primary" onClick={() => getList()}>
            Query
          </Button>
          &nbsp; &nbsp;
          <Button
            onClick={() => {
              form.resetFields();
            }}
          >
            Reset
          </Button>
        </Form.Item>
      </Form>
      <br />
      <br />

      <Table rowKey="id" dataSource={list} columns={columns} />
    </>
  );
}
