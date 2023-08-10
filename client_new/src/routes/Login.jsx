import { Formik, Form, useField,  } from "formik";
import * as Yup from 'yup'
import axios from 'axios'
// import { getURL } from "./Utils";

const TextInput = ({...props}) => {
  const [field, meta] = useField(props);
  return (
    <>
      <input {...field} {...props} className="border-2 " />
      {meta.touched && meta.error ? (
        <div>{meta.error}</div>
      ): null}
    </>
  )
}

const credentialsSchema = Yup.object({
  username: Yup.string()
    .max(20, "Max 20 characters")
    .required('Required!')
    .lowercase("Must be lowercase"),
  password: Yup.string()
    .max(20, "Max 20 characters.")
    .required("Required!")

}).strict(true)

const handleSubmit = (values, {setSubmitting}) => {
  setTimeout(() => {
    alert(JSON.stringify(values, null, 2))
    console.log(import.meta.env.VITE_BACKEND_BASE_URL)
    // axios.post(getURL('/login'), values)
    // axios.post(process.env.REACT_APP_ENV_TEST, values)
    //   .then(res => {
    //     alert(res)
    //   })
    //   .catch(err => alert(err))
    setSubmitting(false)
  }, 400)
}

function Login() {
  return (
    <div className="w-full h-1/2 flex justify-center items-center">
      <Formik
        initialValues={{
          username: '',
          password: '',
        }}
        validationSchema={credentialsSchema}
        onSubmit={handleSubmit}
      >
        <Form className="flex flex-col h-24 justify-evenly">
          <TextInput
            name="username"
            type="text"
            placeholder="Username"
          />
          <TextInput
            name="password"
            type="password"
            placeholder="Password"
          />
          <button type="submit" className="border-2">Login</button>
        </Form>
      </Formik>
    </div>
  );
}

export default Login;