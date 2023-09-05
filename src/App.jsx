/* eslint-disable react/prop-types */
import * as React from "react";

import {
  Routes,
  Route,
  Link,
  useNavigate,
  useLocation,
  Navigate,
  Outlet,
} from "react-router-dom";

import Login from "./views/login";
import { Button, Layout } from "antd";
import style from "./App.module.less";

import logo from "./assets/imgs/logo.png";
import { Dropdown } from "antd";
import { DownOutlined, SmileOutlined } from "@ant-design/icons";
import { Space, Form, Menu } from "antd";
import { useState } from "react";
import { Modal } from "antd";
import { Input } from "antd";

const { Header, Footer, Sider, Content } = Layout;

export default function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/work" element={<LayoutWrap />}>
          <Route index element={<LayoutIndexPage />} />
          {/* <Route path="about" element={<About />} /> */}
        </Route>
      </Routes>
    </>
  );
}

function LayoutWrap() {
  const [pwdVisible, setPwdVisible] = useState(false);

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
                    label: <a>Logout</a>,
                  },
                ],
              }}
            >
              <Space>
                Bom
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
              items={[
                { key: "1", label: "Option 1" },
                { key: "2", label: "Option 2" },
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

function LayoutIndexPage() {
  return <h3>welCome</h3>;
}

const ChangePasswordModal = ({ visible, onCancel }) => {
  const [form] = Form.useForm();
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    try {
      setLoading(true);
      const values = await form.validateFields();
      // 在此处执行密码修改的逻辑
      console.log(values);
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
      footer={[
        <Button key="cancel" onClick={onCancel}>
          Cancel
        </Button>,
        <Button
          key="submit"
          type="primary"
          loading={loading}
          onClick={handleSubmit}
        >
          Submit
        </Button>,
      ]}
    >
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
