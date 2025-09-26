# ERP System

Sistema ERP full-stack con FastAPI backend y Vue.js frontend.

## 🏗️ Arquitectura del Proyecto

```
ERP/
├── README.md              # Este archivo (documentación general)
├── .env.sample           # Variables de entorno ejemplo
├── .gitignore           # Archivos ignorados por Git
├── docs/                # Documentación del proyecto
├── api/                 # Backend FastAPI
│   ├── core/            # Funcionalidades base
│   ├── modules/         # Módulos del negocio
│   ├── shared/          # Utilidades compartidas
│   ├── tests/           # Pruebas backend
│   ├── main.py          # Punto de entrada API
│   ├── requirements.txt # Dependencias Python
│   └── README.md        # Documentación específica de la API
└── frontend/            # Frontend Vue.js (futuro)
    ├── src/
    ├── public/
    ├── package.json
    └── README.md        # Documentación específica del frontend
```

## 🚀 Inicio Rápido

### 1. Clonar repositorio
```bash
git clone <repository-url>
cd ERP
```

### 2. Configurar variables de entorno
```bash
cp .env.sample .env
# Editar .env con tus valores
```

### 3. Ejecutar Backend
```bash
cd api
python -m venv venv
source venv/bin/activate  # Linux/Mac o venv\Scripts\activate en Windows
pip install -r requirements.txt
python main.py
```
🔗 API disponible en: http://localhost:8000

### 4. Ejecutar Frontend (próximamente)
```bash
cd frontend
npm install
npm run dev
```
🔗 Web disponible en: http://localhost:5173

## 📚 Documentación

- **[API Documentation](./api/README.md)** - Guía detallada del backend
- **[Frontend Documentation](./frontend/README.md)** - Guía detallada del frontend (próximamente)

## 🔧 Tecnologías

### Backend
- **FastAPI** - Framework web moderno y rápido
- **Pydantic** - Validación de datos
- **SQLAlchemy** - ORM para base de datos
- **JWT** - Autenticación basada en tokens

### Frontend (próximamente)
- **Vue.js 3** - Framework progresivo de JavaScript
- **Vite** - Build tool rápido

## 🏢 Módulos del Sistema

- ✅ **Users** - Gestión de usuarios y autenticación
- 🚧 **Inventory** - Control de inventarios
- 🚧 **Billing** - Facturación y pagos
- 🚧 **Reports** - Reportes y análisis

## 🔐 Seguridad

- Variables de entorno para configuración sensible
- Autenticación JWT
- Validación de datos con Pydantic
- CORS configurado para desarrollo y producción

## 🤝 Contribución

1. Fork el proyecto
2. Crear branch para feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver [LICENSE](LICENSE) para detalles.

## 📞 Contacto

- Proyecto: [https://github.com/usuario/ERP](https://github.com/usuario/ERP)
- Issues: [https://github.com/usuario/ERP/issues](https://github.com/usuario/ERP/issues)