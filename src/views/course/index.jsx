import { Button, Form } from "antd";
import { Select } from "antd";
import { message } from "antd";
import { Upload } from "antd";
import { Input } from "antd";
import { Table } from "antd";
import React from "react";
import { useState } from "react";

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

  const [list, setList] = useState(dataSource);

  const uploadProps = {
    showUploadList: false,
    name: "file",
    action: "https://www.mocky.io/v2/5cc8019d300000980a055e76",
    headers: {
      authorization: "authorization-text",
    },
    onChange(info) {
      if (info.file.status !== "uploading") {
        console.log(info.file, info.fileList);
      }
      if (info.file.status === "done") {
        message.success(`${info.file.name} file uploaded successfully`);
      } else if (info.file.status === "error") {
        message.error(`${info.file.name} file upload failed.`);
      }
    },
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
      render: () => {
        return (
          <>
            <Upload {...uploadProps}>
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

  return (
    <>
      <Form layout="inline" form={form}>
        <Form.Item label="Course" name="course">
          <Input placeholder="Course Name" />
        </Form.Item>
        <Form.Item label="submission status" name="submission_status">
          <Select style={{ width: "180px" }} placeholder="Submission Status">
            {stateMap.map((item) => (
              <Select.Option value={item.value} key={item.value}>
                {item.label}
              </Select.Option>
            ))}
          </Select>
        </Form.Item>
        <Form.Item>
          <Button
            type="primary"
            onClick={() => {
              const val = form.getFieldsValue();
              const oldData = dataSource.filter(
                (it) =>
                  it.course.includes(val.course) ||
                  it.submission_status == val.submission_status
              );
              setList(oldData);
            }}
          >
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

      <Table rowKey="email" dataSource={list} columns={columns} />
    </>
  );
}
