import React from 'react';
import PropTypes from'prop-types';
import key from 'weak-key';

const Table = ({data}) => !data.length ? (<p>nothing to show</p>) : (
<div className="column">
<p>showing {data.length} data</p> 
<table>
    <thead>
        <tr>
            {
                Object.entries(data[0]).map(el=><th key={key(el)}>{el[0]}</th>)
            }
        </tr>
    </thead>
    <tbody>
        
    </tbody>
</table>
</div>
);

Table.propTypes = {
    data : PropTypes.array.isRequired
};

export default Table;