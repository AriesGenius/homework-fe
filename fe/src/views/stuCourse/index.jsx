import React, { useEffect, useState } from "react";

import { Button, Form, Select, message, Upload, Input, Table } from "antd";

import { apiGetStuCourse, apiSubmitStuCourse } from "../../utils/api";

const user = JSON.parse(localStorage.getItem("user") || "{}");

export default function Index() {
  const dataSource = [
    {
      name: "Aries",
      email: "zhajy154@mymail.unisa.edu.au",
      password: "student1",
      course: ["Systems Design", ", Web Technology"],
      assignment_id: "week1",
      submission_status: "1",
      date: "",
      grade: "",
    },
    {
      name: "Li",
      email: "liyzy092@mymail.unisa.edu.au",
      password: "student2",
      course: ["Python Programing"],
      assignment_id: "week1",
      submission_status: "2",
      date: "",
      grade: "",
    },
    {
      name: "April",
      email: "laumy037@mymail.unisa.edu.au",
      password: "student3",
      course: ["Data Structures", ", Database for the Enterprise"],
      assignment_id: "week1",
      submission_status: "2",
      date: "",
      grade: "",
    },
    {
      name: "McCulloch",
      email: "mcclt001@mymail.unisa.edu.au",
      password: "student4",
      course: ["Python Programing", ", Systems Design"],
      assignment_id: "week1",
      submission_status: "1",
      date: "",
      grade: "",
    },
  ];

  const [list, setList] = useState([]);

  const [fileList, setFileList] = useState([]);

  const uploadProps = {
    showUploadList: false,
    fileList,
  };

  const submitFile = (param) => {
    console.log("param -> :", param);
    const name = new FormData();
    name.append("file", param.file);
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
      dataIndex: "assignment_id",
      key: "assignment_id",
    },
    {
      title: "Course",
      dataIndex: "course",
      key: "course",
    },
    {
      title: "Current Status",
      dataIndex: "submission_status",
      key: "submission_status",
      render: (text) => <>{stateObject[text]}</>,
    },
    {
      title: "Date",
      dataIndex: "address",
      key: "address",
    },
    {
      title: "Grade",
      dataIndex: "address",
      key: "address",
    },
    {
      title: "Operate",
      render: (row) => {
        return (
          <>
            <Upload
              {...uploadProps}
              beforeUpload={(file) => {
                console.log("file -> :", file);
                const { homework_name, homework_course, homework_user } = row;

                submitFile({
                  file,
                  homework_name,
                  homework_course,
                  homework_user,
                });
                return false;
              }}
            >
              <Button>Submiting</Button>
            </Upload>
            &nbsp; &nbsp;
            <Button type="link">Faceback</Button>
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
      homework_user: user.username,
      homework_course: form.getFieldValue("course"),
    }).then((res) => {
      setList(res.data?.homeworks || []);
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
              setList(dataSource);
            }}
          >
            Reset
          </Button>
        </Form.Item>
      </Form>
      <br />
      <br />

      <Table rowKey="email" dataSource={dataSource} columns={columns} />
    </>
  );
}
