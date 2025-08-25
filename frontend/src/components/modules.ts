import PackageIcon from "./icons/PackageIcon";
import ShoppingCartIcon from "./icons/ShoppingCartIcon";
import UsersIcon from "./icons/UsersIcon";
import BarChartIcon from "./icons/BarChart";
import SettingsIcon from "./icons/SettingsIcon";
import DollarSignIcon from "./icons/DollarSignIcon";
import HomeIcon from "./icons/HomeIcon";

export const modules = {
    dashboard: {
        name: 'Dashboard',
        icon: HomeIcon,
        subcategories: ['Resumen General', 'KPIs', 'Gráficos']
    },
    inventario: {
        name: 'Inventario',
        icon: PackageIcon,
        subcategories: ['Productos', 'Categorías', 'Operaciones', 'Reportes', 'Stock Mínimo']
    },
    ventas: {
        name: 'Ventas',
        icon: ShoppingCartIcon,
        subcategories: ['Pedidos', 'Facturación', 'Clientes', 'Cotizaciones', 'Historial']
    },
    contabilidad: {
        name: 'Contabilidad',
        icon: DollarSignIcon,
        subcategories: ['Cuentas', 'Transacciones', 'Balance', 'Reportes Fiscales', 'Presupuestos']
    },
    recursos: {
        name: 'Recursos Humanos',
        icon: UsersIcon,
        subcategories: ['Empleados', 'Nómina', 'Horarios', 'Vacaciones', 'Evaluaciones']
    },
    reportes: {
        name: 'Reportes',
        icon: BarChartIcon,
        subcategories: ['Ventas', 'Inventario', 'Financiero', 'RRHH', 'Personalizado']
    },
    configuracion: {
        name: 'Configuración',
        icon: SettingsIcon,
        subcategories: ['Sistema', 'Usuarios', 'Permisos', 'Backup', 'Integrations']
    }
};
