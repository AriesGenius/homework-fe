import { Button, Form } from "antd";
import { Select } from "antd";
import { message } from "antd";
import { Upload } from "antd";
import { Input } from "antd";
import { Table } from "antd";
import React from "react";

export default function Index() {
  const dataSource = [
    {
      key: "1",
      status: "1",
      name: "12313",
      age: 32,
      address: "address",
    },
    {
      key: "2",
      status: "2",
      name: "489498",
      age: 42,
      address: "address",
    },
  ];

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
      dataIndex: "name",
      key: "name",
    },
    {
      title: "Course",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "Current Status",
      dataIndex: "status",
      key: "status",
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
        <Form.Item label="submission status">
          <Select style={{ width: "180px" }} placeholder="Submission Status">
            {stateMap.map((item) => (
              <Select.Option value={item.value} key={item.value}>
                {item.label}
              </Select.Option>
            ))}
          </Select>
        </Form.Item>
        <Form.Item>
          <Button type="primary">Query</Button>
          &nbsp; &nbsp;
          <Button>Reset</Button>
        </Form.Item>
      </Form>
      <br />
      <br />

      <Table dataSource={dataSource} columns={columns} />
    </>
  );
}
