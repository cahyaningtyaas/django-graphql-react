import React , { Component } from 'react';
import PropTypes from 'prop-types';

class DataProvider extends Component {
    static propTypes = {
        endpoints : PropTypes.string.isRequired, 
        render: PropTypes.func.isRequired
    };
    state = {
        data: [],
        loaded: false,
        placeholder: 'loading...'
    };
    componentDidMount(){
        fetch(this.props.endpoints).then(response=>{
            if (response.status !== 200){
                return this.setState({
                    placeholder: 'something wentwrong'
                });
            } return response.json();
        }).then(data=>
            this.setState({
                data: data,
                loaded: true
            })
        );
    }
    render(){
        const{
            data,loaded, placeholder
        } = this.state;
        return loaded ? this.props.render(data): <p>{placeholder}</p>;
    }
}

export default DataProvider;