FROM node:18-alpine AS builder

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install --frozen-lockfile

COPY . .

RUN yarn build

FROM node:18-alpine AS runner

WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile --production

COPY --from=builder /app/.next ./.next
COPY --from=builder /app/package.json ./package.json

EXPOSE 3000

CMD ["yarn", "start"]