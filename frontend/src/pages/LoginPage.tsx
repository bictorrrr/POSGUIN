import { useState } from "react"
import { useNavigate } from "react-router-dom"
import "./CSS/LoginPage.css"
import Button from "../components/Button"
import Input from "../components/Input"
import Clock from "../components/Clock"


function LoginPage() {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const navigate = useNavigate()

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault()
        console.log("Login con:", { email, password })
        //TODO -> Logica de inicio de sesion
        navigate("/dashboard")
    }

    return (
        <div className="login-container">
            <Clock />
            <form onSubmit={handleSubmit} className="login-form">
                <h1>POSGUIN</h1>
                <h2>Inicio de Sesion</h2>
                <Input
                    type="email"
                    placeholder="Correo Electronico"
                    variant="modal"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input
                    type="password"
                    placeholder="Contraseña"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <Button type="submit">Ingresar</Button>
            </form>
        </div>
    )
}

export default LoginPage
