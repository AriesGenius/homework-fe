 // Importing UI components from 'antd'
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
import React, { useEffect, useState } from "react";// Importing React and hooks
import { apiGetTeaCourse, apiNewWork } from "../../utils/api";// Importing API utility functions

export default function Index() {
  // Retrieving user data from local storage
  const user = JSON.parse(localStorage.getItem("user") || "{}");
  // State to manage the list of courses
  const [list, setList] = useState([]);
    // State to manage work modal (open/closed status and row data)
  const [workState, setWorkState] = useState({
    open: false,
    row: {},

    onCreate: (data) => {  // Function called when a new work is created
      apiNewWork({// API call to create new work
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

  // Column definitions for the table
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
  // Function to fetch and set the list of courses
  const getList = () => {
    apiGetTeaCourse({
      course_teacher: user.username,
    }).then((res) => {
      setList(res.data?.courses || []);
    });
  };
  // useEffect hook to fetch course list on component mount
  useEffect(() => {
    getList();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <>
      <Table rowKey="id" dataSource={list} columns={columns} />

      <AddWorkModal {...workState} />
    </>
  );
}

// eslint-disable-next-line react/prop-types
// AddWorkModal component for adding new course works
const AddWorkModal = ({ open, onCreate, onCancel, row }) => {
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);// State for loading indicator
  
  // Function to handle modal 'OK' action
  const handleOk = () => {
    setLoading(true);// Start loading
    form
      .validateFields()// Validate form fields
      .then((values) => {
        onCreate({ ...values, ...row });// Call onCreate with form values and row data
        setLoading(false);// Stop loading
        form.resetFields();// Reset form fields
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
