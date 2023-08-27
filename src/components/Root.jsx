import { Outlet } from "react-router-dom";
import { Authenticator} from '@aws-amplify/ui-react'

function Root() {
    return (
        <>
          <Authenticator>
            {({ signOut, user}) => (
                <div className="h-screen w-screen flex">
                    <div className="h-full grid grid-rows-7 w-28 bg-gray-300">
                        {
                        ["Home", "Papers", "Notes", "People", "Groups", "Settings"]
                        .map((e) => 
                            <a
                            className="flex justify-center items-center hover:bg-gray-400"
                            href={'/'+e.toLowerCase()}
                            >
                                {e}
                            </a>
                
                            )
                        }
                        <button 
                        className="flex justify-center items-center hover:bg-gray-400 truncate"
                        onClick={signOut}
                        >
                            {"Sign Out " + user.attributes.email}
                        </button>
                    </div>
                    <Outlet/>
                </div>
            )}
          </Authenticator>
        </>
    );
}

export default Root;