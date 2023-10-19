import {
  Button,
  Divider,
  Form,
  Select,
  message,
  Upload,
  Input,
  Table,
  Modal,
} from "antd";
import React, { useEffect, useState } from "react";
import { apiGetTeaCourse, apiNewWork } from "../../utils/api";

export default function Index() {
  const user = JSON.parse(localStorage.getItem("user") || "{}");

  const [list, setList] = useState([]);

  const [workState, setWorkState] = useState({
    open: false,
    row: {},

    onCreate: (data) => {
      apiNewWork({
        course_name: data.course_name,
        course_homework: data.course_homework,
      }).then((res) => {
        message.success("Add Success");

        const old = { ...workState };
        setWorkState({ ...old, open: false, row: {} });
      });
    },
    onCancel: () => {
      const old = { ...workState };
      setWorkState({ ...old, open: false, row: {} });
    },
  });

  const columns = [
    {
      title: "No.",
      dataIndex: "id",
      key: "id",
    },
    {
      title: "course_name",
      dataIndex: "course_name",
      key: "course_name",
    },
    {
      title: "course_teacher",
      dataIndex: "course_teacher",
      key: "course_teacher",
    },
    {
      title: "Operate",
      render: (row) => {
        return (
          <>
            <Button
              onClick={() => {
                const old = { ...workState };
                setWorkState({ ...old, open: true, row });
              }}
            >
              Add Work
            </Button>
            &nbsp; &nbsp;
            <Button type="link" href={`/work/work-list?course_name=${row.course_name}`}>
              Works
            </Button>
          </>
        );
      },
    },
  ];

  const [form] = Form.useForm();

  const getList = () => {
    apiGetTeaCourse({
      course_teacher: user.username,
    }).then((res) => {
      setList(res.data?.courses || []);
    });
  };

  useEffect(() => {
    getList();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <>
      {/* <Button type="primary">Add Course</Button> */}
      {/* <Divider /> */}
      {/* 
      <br />
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
      */}

      <Table rowKey="id" dataSource={list} columns={columns} />

      <AddWorkModal {...workState} />
    </>
  );
}

// eslint-disable-next-line react/prop-types
const AddWorkModal = ({ open, onCreate, onCancel, row }) => {
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);

  const handleOk = () => {
    setLoading(true);
    form
      .validateFields()
      .then((values) => {
        onCreate({ ...values, ...row });
        setLoading(false);
        form.resetFields();
      })
      .catch(() => {
        setLoading(false);
      });
  };

  return (
    <Modal
      open={open}
      title="Add Course"
      okText="Add"
      confirmLoading={loading}
      onCancel={onCancel}
      onOk={handleOk}
    >
      <Form form={form} layout="vertical">
        <Form.Item
          name="course_homework"
          label="Course Homework"
          rules={[
            { required: true, message: "Please enter a course homework" },
          ]}
        >
          <Input />
        </Form.Item>
      </Form>
    </Modal>
  );
};
