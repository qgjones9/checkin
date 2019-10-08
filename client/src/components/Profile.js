import React, { Component } from 'react';
import '../App.css'
import {Table, Button } from 'reactstrap'
import LoginControl from './CheckinControl'

export default class Profile extends Component {
    constructor(props) {
        super(props)

        this.state = {
            parents: [],
            children: []
        }

    }

    componentDidMount() {
        this.fetchParent()
    }

    async fetchParent() {
        const response = await fetch('https://5d9be2b2686ed000144d24cb.mockapi.io/api/v1/parent');
        const json = await response.json()

        let children = []
        json[0].child.map(child => {
            let data = {
                parentId: child.parentId,
                avatar: child.avatar,
                createdAt: child.createdAt,
                grade: child.grade,
                name: child.name,
                status: child.status
            }
            children.push(data)
        })

        if (json) {
            this.setState({
                parents: json[0],
                children: children
            })
            console.log('successfully set parent state')
        }else{
            console.log('something went wrong when fetching data')
        }
    }

    populateTableWithChildren(){
        return this.state.children.map((child) => {
            const { parentId, name, avatar, grade, createdAt } = child
            return (
                <tr key={parentId}>
                  <td>{name}</td>
                  <td>{grade}</td>
                  <td> <LoginControl /> </td>
                </tr>
            )
        })
    }


    render() {
        return (

            <div className="container">
                <div className="profile profile-header">
                    <div className="parent parent-avatar">
                        <img src={this.state.parents.avatar} alt=""/>
                    </div>
                    <div className="parent parent-title">
                        <h2>Welcome {this.state.parents.PrimaryParent}!</h2>
                    </div>
                </div>
                <div className="children">
                    <Table responsive>
                          <thead>
                            <tr>
                              <th>Name</th>
                              <th>Grade</th>
                              <th>Status</th>
                            </tr>
                          </thead>
                          <tbody>
                          {this.populateTableWithChildren()}
                          </tbody>
                        </Table>
                </div>
            </div>
        );
    }
}
