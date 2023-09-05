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

export default function Index() {

  const nav = useNavigate();
  
  const onFinish = (values) => {
    console.log(values);


    nav('/work')
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
            <Form.Item
              label="Type"
              name="type"
              rules={[{ required: true, message: "Please input your email!" }]}
              initialValue={"1"}
            >
              <Select>
                <Select.Option value="1">Student</Select.Option>
                <Select.Option value="2">Teacher</Select.Option>
              </Select>
            </Form.Item>

            <Form.Item
              label="Email"
              name="email"
              rules={[{ required: true, message: "Please input your email!" }]}
              initialValue={"email"}
            >
              <Input type="text" placeholder="email" />
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
              initialValue={"password"}
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
              <a href="/register">Register</a>
            </p>
          </Form>
        </Col>
      </Row>
    </div>
  );
}
