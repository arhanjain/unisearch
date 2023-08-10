import { Outlet, Link } from "react-router-dom";

function Root() {
  return (
    <div className="h-screen w-screen">
      <div className="w-full h-10 bg-red-500 flex justify-evenly items-center">
        <Link to={'/'}>Home</Link>
        <Link to={'/login'} className="underline">Login</Link>
      </div>
      <Outlet />
    </div>
  );
}

export default Root;