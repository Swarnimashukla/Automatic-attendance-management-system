// import every file to built the complete route
import Navbar from "./Navbar/Navbar";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Home } from "./Link/home";
import { About } from "./Link/about";
import { Demo } from "./Link/demo";
import { Login } from "./Link/login";
import { Features } from "./Link/features";
import { Pricing } from "./Link/pricing";

function Site() {
  return (
    <>
      <Router>
        <NavBar />

        <div className="Link">
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/about" component={About} />
            <Route path="/demo" component={Demo} />
            <Route path="/login" component={Login} />
            <Route path="/features" component={Features} />
            <Route path="/pricing" component={Pricing} />
          </Switch>
        </div>
      </Router>
    </>
  );
}

export default Site;