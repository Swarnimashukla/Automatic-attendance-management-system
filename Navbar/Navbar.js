import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import "./Navbar.css";
import logo from '.Resource/Logo_Design1 _Garvitraj_Pandey.png';

function Navbar() {
  const [click, setClick] = useState(false);

  const handleClick = () => setClick(!click);
  return (
    <>
      <nav className="navbar">
        <div className="nav">
          <NavLink exact to="/">
            <img src={logo} alt="logo" width="157.83" height="165"/>
          </NavLink>

          <ul className={click ? "active navmenu" : "navmenu"}>
            <li className="nav-option">
              <NavLink
                exact
                to="/"
                activeClassName="active"
                className="link-nav"
                onClick={handleClick}
              >
                Home
              </NavLink>
            </li>
            <li className="nav-option">
              <NavLink
                exact
                to="/features"
                activeClassName="active"
                className="link-nav"
                onClick={handleClick}
              >
                Features
              </NavLink>
            </li>
            <li className="nav-option">
              <NavLink
                exact
                to="/pricing"
                activeClassName="active"
                className="link-nav"
                onClick={handleClick}
              >
                Pricing
              </NavLink>
            </li>
            <li className="nav-option">
              <NavLink
                exact
                to="/demo"
                activeClassName="active"
                className="link-nav"
                onClick={handleClick}
              >
                Demo
              </NavLink>
            </li>
            <li className="nav-option">
              <NavLink
                exact
                to="/login"
                activeClassName="active"
                className="link-nav"
                onClick={handleClick}
              >
                Login
              </NavLink>
            </li>
          </ul>
          <div className="nav-block" onClick={handleClick}>
          </div>
        </div>
      </nav>
    </>
  );
}

export default Navbar;