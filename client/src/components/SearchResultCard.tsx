export interface SearchResult {
    title: string,
    authors: Array<string>,
    link: string,
}

type InputTypes = {
    data: SearchResult,
}

function SearchResultCard({data} : InputTypes) {
    return ( 
        <div className="w-full h-fill rounded-md border-solid border-2 border-red-500 my-2 p-1">
            <div className="text-sm whitespace-nowrap truncate">{data.title}</div>
            <div className="text-sm whitespace-nowrap truncate">{data.authors.join(", ")}</div>
            <div className="text-sm whitespace-nowrap truncate">{data.link}</div>
        </div>
    );
}

export default SearchResultCard;