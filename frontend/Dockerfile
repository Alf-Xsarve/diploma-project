FROM node:20 AS builder

WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

RUN npm run build

FROM node:20

COPY --from=builder /app/dist /usr/share/html

CMD ["npm", "run", "dev", "--", "--host"]