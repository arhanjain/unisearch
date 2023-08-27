
function SearchResultCard({data}) {
    return ( 
        <div className=" w-full h-full grid grid-cols-8 rounded-md border-solid border-2 border-black my-2 p-2">
            <div className=" flex-col truncate col-span-7">
                <a className="text-sm whitespace-nowrap" href={data.link}>{data.title}</a>
                <div className="text-sm whitespace-nowrap truncate">{data.authors.join(", ")}</div>
            </div>
            <div className="h-full w-full flex justify-center items-center">
                <p className=" text-sm text-center">Save</p>
            </div>
        </div>
    );
}

export default SearchResultCard;