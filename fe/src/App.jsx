/* eslint-disable react/prop-types */
import * as React from "react";

// Importing components and hooks from react-router-dom for routing purposes
import {
  Routes,
  Route,
  Link,
  useNavigate,
  useLocation,
  Navigate,
  Outlet,
} from "react-router-dom";

// Importing custom components and styles
import Login from "./views/login/Index";
import { Button, Layout } from "antd";
import style from "./App.module.less";

// Importing assets and UI components from antd and ant-design/icons
import logo from "./assets/imgs/logo.png";
import { Dropdown } from "antd";
import {
  DownOutlined,
  EditOutlined,
  HomeOutlined,
  SmileOutlined,
} from "@ant-design/icons";
import { Space, Form, Menu } from "antd";
import { useState } from "react";
import { Modal } from "antd";
import { Input } from "antd";

// Destructuring Layout component to use its subcomponents
const { Header, Footer, Sider, Content } = Layout;

// Importing subcomponents for different routes
import StuCourse from "./views/stuCourse";
import TeaCourse from "./views/teaCourse";
import TeaWork from "./views/teaWork";

// Main App component defining the routing structure of the application
export default function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/work" element={<LayoutWrap />}>
          <Route index element={<LayoutIndexPage />} />
          <Route path="stu-courses" element={<StuCourse />} />
          <Route path="tea-courses" element={<TeaCourse />} />
          <Route path="work-list" element={<TeaWork />} />
          {/* <Route path="about" element={<About />} /> */}
        </Route>
      </Routes>
    </>
  );
}

// LayoutWrap component that renders the main layout including header, sidebar, and content area
function LayoutWrap() {
  // State to control visibility of the change password modal
  const [pwdVisible, setPwdVisible] = useState(false);
  // Retrieving user data from localStorage
  const user = JSON.parse(localStorage.getItem("user") || "{}");

  // Hook for programmatically navigating between routes
  const navigate = useNavigate();
  return (
    <>
      <Layout>
        <Header className={style.header}>
          <div className={style.logo}>
            <img src={logo} alt="" />
          </div>
          <div className={style.names}>
            <Space>welcome,</Space>
            <Dropdown
              trigger={["click"]}
              menu={{
                items: [
                  {
                    key: "1",
                    label: (
                      <a
                        onClick={() => {
                          setPwdVisible(true);
                        }}
                      >
                        Change Password
                      </a>
                    ),
                  },
                  {
                    key: "2",
                    label: (
                      <a
                        href="/"
                        onClick={() => {
                          localStorage.clear();
                          navigate("/");
                        }}
                      >
                        Logout
                      </a>
                    ),
                  },
                ],
              }}
            >
              <Space>
                {user?.username || ""}
                <DownOutlined />
              </Space>
            </Dropdown>
          </div>
        </Header>
        <Layout hasSider>
          <Sider className={style.leftSide}>
            <Menu
              defaultSelectedKeys={["1"]}
              defaultOpenKeys={["sub1"]}
              mode="inline"
              onClick={({ key }) => {
                navigate(key);
              }}
              items={[

                user.type == 1 && {
                  key: "/work/stu-courses",
                  label: "Student Courses",
                  icon: <EditOutlined />,
                },
                user.type == 2 && {
                  key: "/work/tea-courses",
                  label: "Teacher Courses",
                  icon: <EditOutlined />,
                },
              ]}
            />
          </Sider>
          <Content className={style.content}>
            <Outlet />
          </Content>
        </Layout>
      </Layout>

      <ChangePasswordModal
        visible={pwdVisible}
        onCancel={() => setPwdVisible(false)}
      />
    </>
  );
}

// Placeholder component for the layout index page
function LayoutIndexPage() {
  return <h3>welCome</h3>;
}

// ChangePasswordModal component for handling password changes
const ChangePasswordModal = ({ visible, onCancel }) => {
  // Form and loading state initialization
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);

   // Function to handle the submit event of the form
  const handleSubmit = async () => {
    try {
      // Set loading to true to indicate process initiation
      setLoading(true);
      // Validate form fields and retrieve their values
      const values = await form.validateFields();
      // Logic for password change should be implemented here
      // Currently, it logs the form values to the console
      console.log(values);
      // Reset loading state after operation
      setLoading(false);
    } catch (error) {
      console.error(error);
      setLoading(false);
    }
  };

  return (
    <Modal
      destroyOnClose
      maskClosable={false}
      open={visible}
      width="38%"
      centered
      title="Change Password"
      onCancel={onCancel}

      // Defines the buttons at the bottom of the modal
      footer={[
        // 'Cancel' button to close the modal without submitting
        <Button key="cancel" onClick={onCancel}>
          Cancel
        </Button>,
         // 'Submit' button that triggers the handleSubmit function
        <Button
          key="submit"
          type="primary"
          loading={loading}  // Shows a loading indicator on the button based on the 'loading' state
          onClick={handleSubmit}
        >
          Submit
        </Button>,
      ]}
    >
      {/* Form for password change, utilizing Ant Design's Form component */}
      <Form form={form} layout="vertical">
        <Form.Item
          name="oldPassword"
          label="Old Password"
          rules={[
            { required: true, message: "Please enter your old password" },
          ]}
        >
          <Input.Password />
        </Form.Item>
        <Form.Item
          name="newPassword"
          label="New Password"
          rules={[
            { required: true, message: "Please enter your new password" },
          ]}
        >
          <Input.Password />
        </Form.Item>
      </Form>
    </Modal>
  );
};
