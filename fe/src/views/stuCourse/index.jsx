// Importing React hooks, Ant Design components, and  API functions
import React, { useEffect, useState } from "react";
import { Button, Form, Select, message, Upload, Input, Table } from "antd";
import { apiGetStuCourse, apiSubmitStuCourse } from "../../utils/api";

// Retrieving user data from local storage
const user = JSON.parse(localStorage.getItem("user") || "{}");

// Main functional component 
export default function Index() {
   // State for maintaining the list of courses and uploaded files
  const [list, setList] = useState([]);
  const [fileList, setFileList] = useState([]);

   // Function to handle file submission
  const submitFile = (param) => {
    console.log("param -> :", param);
    console.log("fileList -> :", fileList);

    // Creating a FormData object for file upload
    const name = new FormData();
    fileList.forEach((file) => {
      name.append("file[]", file);
    });
    name.append("homework_name", param.homework_name);
    name.append("homework_course", param.homework_course);
    name.append("homework_user", param.homework_user);

    // Calling the API function to submit the homework
    apiSubmitStuCourse(name).then((res) => {
      console.log("res -> :", res);
    });
  };

  // Column definitions for the Ant Design Table component
  const columns = [
    // Columns for course details
    // Each column defines how each field in the data should be displayed
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
    {
      title: "Date",
      dataIndex: "homework_time",
      key: "homework_time",
    },
    // Column for file upload and feedback link
    {
      title: "Operate",
      render: (row) => {
        return (
          <>
            <Upload
            // Upload component configuration
              showUploadList={false}
              name="file"
              action="/api/user/submit_homework"
              fileList={fileList}
              accept={".jpg, .jpeg, .png,.uxf"}
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
              // Function to handle file upload
              beforeUpload={(file) => {
                if (
                  file.type !== "image/png" &&
                  file.type !== "image/jpeg" &&
                  file.type !== "image/jpg" &&
                  !file.name.includes(".uxf")
                ) {
                  message.error(`${file.name} must is png,jpg,uxl file`);
                  return false;
                }

            
              }}
            >
              <Button>Submiting</Button>
            </Upload>
            &nbsp; &nbsp;
            {/*  Link to download feedback, if available*/}
            {row.submit && (
              // eslint-disable-next-line react/jsx-no-target-blank
              <a type="link" href={row.homework_score} target="_blank" >
                Feedback
              </a>
            )}
          </>
        );
      },
    },
  ];

  // Mapping state values to labels for display
  const stateMap = [
    { label: "submitted", value: "1" },
    { label: "uncommitted", value: "2" },
  ];

  // Converting stateMap array to an object for easy access
  const stateObject = stateMap.reduce((obj, item) => {
    obj[item.value] = item.label;
    return obj;
  }, {});

  // Initializing form controls
  const [form] = Form.useForm();

  // Function to fetch and set the list of courses
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
        {/* Form item for inputting the course name */}
        <Form.Item label="Course" name="course">
          <Input placeholder="Course Name" />
        </Form.Item>

        {/* Form items for query and reset buttons */}
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
