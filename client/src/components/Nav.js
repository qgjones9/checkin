import React from 'react';
import '../App';
import {Link} from 'react-router-dom'

function Nav() {

    const navStyle = {
        color: 'white'
    }
    return (

        <nav>
            <h3>MPCA</h3>
            <ul className="nav-links">
                <Link style={navStyle} to="/" >
                    <li>Home</li>
                </Link>
                <Link style={navStyle} to="/account" >
                    <li>Account</li>
                </Link>
                <Link style={navStyle} to="/admin" >
                    <li>Admin</li>
                </Link>
                <Link style={navStyle} to="/profile" >
                    <li>Profile</li>
                </Link>
            </ul>
        </nav>
    );
}

export default Nav;