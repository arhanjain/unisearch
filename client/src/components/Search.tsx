import React, { Component, useCallback, useState } from 'react';
import axios from 'axios';
import {debounce} from 'lodash';
import SearchResultCard, {SearchResult} from './SearchResultCard';

type InputTypes = {
    classNames: string,
}

function Search({classNames}: InputTypes) {
    const [articles, setArticles] = useState<Array<SearchResult>>([])
    
    const searchChange = (text: string) => {
            axios.get('/search-articles', {params: {query:text}}).then(res => {
                setArticles(res.data.results)
            }) 
    }

    const delayedSearch = useCallback(
        debounce(text => searchChange(text), 500),
        []
    )

    return (
        <div className={classNames}>
            <input 
                onChange={e => delayedSearch(e.target.value)}
                className='shadow appearance-none border rounded 
                w-full py-2 px-3 text-gray-700 leading-tight 
                focus:outline-none focus:shadow-outline'
            ></input>
            {articles.map(article => {
                return(<SearchResultCard data={article}></SearchResultCard>)
            })}
        </div>
    );
}

export default Search;