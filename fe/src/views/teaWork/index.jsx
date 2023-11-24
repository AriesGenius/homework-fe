// Importing components from Ant Design and React hooks
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
import { apiGetWork, apiDelWork } from "../../utils/api";
import { useSearchParams } from "react-router-dom";

export default function Index() {
  // Retrieving user data from local storage
  const user = JSON.parse(localStorage.getItem("user") || "{}");
  // Hook to access search parameters from URL
  const [search] = useSearchParams();
  // State to store the list of course works
  const [list, setList] = useState([]);

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
      title: "course_homework",
      dataIndex: "course_homework",
      key: "course_homework",
    },
    {
      title: "Operate",
      render: (row) => {
        return (
          <>
            <Button
              onClick={() => {
                apiDelWork({
                  homework_id: row.id,
                }).then((res) => {
                  message.success("Delete Success");
                  getList();
                });
              }}
            >
              delete Work
            </Button>
          </>
        );
      },
    },
  ];

  const [form] = Form.useForm();
  // Function to fetch the list of course works
  const getList = () => {
    apiGetWork({
      course_name: search.get("course_name"),
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
      <Table rowKey="id" dataSource={list} columns={columns} />
    </>
  );
}
