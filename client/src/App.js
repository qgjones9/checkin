import React, { Component } from 'react';
import './App.css';
import Nav from './components/Nav';
import Home from './components/Home';
import Account from './components/Account';
import Admin from './components/Admin'
import {BrowserRouter, Route, Switch} from "react-router-dom";
import Profile from './components/Profile'



class App extends Component {
  render () {
    return (
      <div className="container">
        <div className="row">
          <div className="col-lg-12 mx-auto">
            <BrowserRouter>
              <Nav />
              <Switch>
                <Route path="/" exact component={Home}/>
                <Route path="/admin" component={Admin}/>
                <Route path="/account" exact component={Account}/>
                <Route path="/profile" component={Profile}/>
              </Switch>
            </BrowserRouter>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
