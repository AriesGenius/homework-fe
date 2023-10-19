import { Button, Col, Row } from "antd";
import React from "react";
import style from "./login.module.less";
import logo from "./../../assets/imgs/logo.png";
import { Form, Input, Select } from "antd";

import {
  Routes,
  Route,
  Link,
  useNavigate,
  useLocation,
  Navigate,
  Outlet,
} from "react-router-dom";
import { useState } from "react";
import { message } from "antd";
import { apiLogin, apiReg } from "../../utils/api";

export default function Index() {
  const [isLogin, setIsLogin] = useState(true);

  const nav = useNavigate();

  const onFinish = (values) => {
    if (isLogin) {
      apiLogin(values).then((res) => {
        console.log("res -> :", res);
        if (res.code === 200) {
          message.success("login success");
          localStorage.setItem("user", JSON.stringify(res.data));
          if (res.data.type == 1) {
            nav("/work/stu-courses");
          } else {
            nav("/work/tea-courses");
          }
        } else {
          message.error("login failed");
        }
      });
    } else {
      apiReg(values).then((res) => {
        console.log("res -> :", res);
        if (res.code === 200) {
          message.success("Register success");
          setIsLogin(true);
        } else {
          message.error("Register failed");
        }
      });
    }
  };

  return (
    <div className={style.wrap}>
      <Row>
        <Col span={17} className={style.left}></Col>
        <Col span={7} className={style.right}>
          <img src={logo} alt="" />
          <br />
          <br />
          <br />
          <br />
          <Form
            style={{ width: "90%" }}
            labelAlign="left"
            labelCol={{ span: 8 }}
            onFinish={onFinish}
          >
            {isLogin ? (
              <>
                <Form.Item
                  label="usertype"
                  name="usertype"
                  rules={[
                    { required: true, message: "Please input your email!" },
                  ]}
                >
                  <Select>
                    <Select.Option value="1">Student</Select.Option>
                    <Select.Option value="2">Teacher</Select.Option>
                  </Select>
                </Form.Item>

                <Form.Item
                  label="username"
                  name="username"
                  rules={[
                    { required: true, message: "Please input your username!" },
                  ]}
                >
                  <Input type="text" placeholder="username" />
                </Form.Item>
                <Form.Item
                  label="Password"
                  name="password"
                  rules={[
                    {
                      required: true,
                      message: "Please input your Password!",
                    },
                  ]}
                >
                  <Input type="text" placeholder="Password" />
                </Form.Item>

                <br />
                <br />

                <Form.Item>
                  <Button
                    block
                    htmlType="submit"
                    type="primary"
                    className={style.btn}
                  >
                    Login
                  </Button>
                </Form.Item>

                <p style={{ textAlign: "right" }}>
                  <Button
                    type="link"
                    onClick={() => {
                      setIsLogin(false);
                    }}
                  >
                    No account? Register now
                  </Button>
                </p>
              </>
            ) : (
              <>
                <Form.Item
                  label="usertype"
                  name="type"
                  rules={[
                    { required: true, message: "Please Select Your Type!" },
                  ]}
                >
                  <Select>
                    <Select.Option value="1">Student</Select.Option>
                    <Select.Option value="2">Teacher</Select.Option>
                  </Select>
                </Form.Item>

                <Form.Item
                  label="username"
                  name="username"
                  rules={[
                    { required: true, message: "Please input your username!" },
                  ]}
                >
                  <Input type="text" placeholder="username" />
                </Form.Item>

                <Form.Item
                  label="useremail"
                  name="useremail"
                  rules={[
                    { required: true, message: "Please input your useremail!" },
                  ]}
                >
                  <Input type="text" placeholder="useremail" />
                </Form.Item>

                <Form.Item
                  label="Password"
                  name="password"
                  rules={[
                    {
                      required: true,
                      message: "Please input your Password!",
                    },
                  ]}
                >
                  <Input type="text" placeholder="Password" />
                </Form.Item>

                <Form.Item>
                  <Button
                    block
                    htmlType="submit"
                    type="primary"
                    className={style.btn}
                  >
                    Register
                  </Button>
                </Form.Item>

                <p style={{ textAlign: "right" }}>
                  <Button
                    type="link"
                    onClick={() => {
                      setIsLogin(true);
                    }}
                  >
                    Sign in with an account
                  </Button>
                </p>
              </>
            )}
          </Form>
        </Col>
      </Row>
    </div>
  );
}
