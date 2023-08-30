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

export default function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/work" element={<Layout />}>
          <Route index element={<PublicPage />} />
          <Route path="about" element={<About />} />
        </Route>
      </Routes>
    </>
  );
}

function Layout() {
  return (
    <>
      <ul>
        <li>
          <Link to="/">Public Page</Link>
        </li>
        <li>
          <Link to="/protected">Protected Page</Link>
        </li>
      </ul>
      right
      <Outlet />
    </>
  );
}

function PublicPage() {
  return <h3>Public</h3>;
}

function About() {
  return <h3>About</h3>;
}
