import React, {Component} from 'react'

export function LoginButton(props) {
  return (
    <button onClick={props.onClick}>
      Loggin
    </button>
  );
}

export function LogoutButton(props) {
  return (
    <button onClick={props.onClick}>
      Loggedout
    </button>
  );
}

