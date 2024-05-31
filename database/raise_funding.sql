SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

-- Name: signup; Type: TABLE; Schema: public; Owner: postgres

CREATE TABLE public.signup (
    id SERIAL NOT NULL,
    username varchar(45) NOT NULL,
    hashed_password varchar(100) NOT NULL,
    email text NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL
);
ALTER TABLE public.signup OWNER TO postgres;

-- Name: campaign; Type: TABLE; Schema: public; Owner: postgres

CREATE TABLE public.campaign(
    campaign_id SERIAL NOT NULL,
    title text NOT NULL,
    description text NOT NULL,
    goal_amount decimal NOT NULL, 
    raised_amount decimal NOT NULL,
    start_date date NOT NULL,
    end_date date NOT NULL,
    category text NOT NULL,
    media bytea NOT NULL,
    status varchar(45)
);
ALTER TABLE public.campaign OWNER TO postgres;

-- Name: donator; Type: TABLE; Schema: public; Owner: postgres

CREATE TABLE public.user (
    user_id SERIAL NOT NULL,
    email text NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
);
ALTER TABLE public.user OWNER TO postgres;

-- Name: donation; Type: TABLE; Schema: public; Owner: postgres

CREATE TABLE public.donation (
    donation_id SERIAL NOT NULL,
    campaign_id integer NOT NULL,
    donator_id integer NOT NULL,
    donation_amount decimal NOT NULL,
    donation_date date NOT NULL,
    message_leaving text NOT NULL
);

ALTER TABLE public.donation OWNER TO postgres;

-- Name: newsfeed; Type: TABLE; Schema: public; Owner: postgres

CREATE TABLE public.newsfeed (
    newsfeed_id SERIAL NOT NULL,
    author varchar(45) NOT NULL,
    headline text NOT NULL,
    summary text NOT NULL,
    media bytea NOT NULL,
    publish_date date NOT NULL,
    category text NOT NULL,
    author_id integer
);

ALTER TABLE public.newsfeed OWNER TO postgres;

-- Name: siginin; Type: TABLE; Schema: public; Owner: postgres

CREATE TABLE public.signin (
    id SERIAL NOT NULL,
    username varchar(45) NOT NULL,
    password varchar(45) NOT NULL
);

ALTER TABLE public.signin OWNER TO postgres;

-- Primary Key; Schema: public; Owner: postgres

ALTER TABLE ONLY public.campaign
    ADD CONSTRAINT camapaign_pkey PRIMARY KEY (campaign_id);

ALTER TABLE ONLY public.newsfeed
    ADD CONSTRAINT newsfeed_pkey PRIMARY KEY (newsfeed_id);

ALTER TABLE ONLY public.donation
    ADD CONSTRAINT donation_pkey PRIMARY KEY (donation_id);

ALTER TABLE ONLY public.user
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_id);

ALTER TABLE ONLY public.signin
    ADD CONSTRAINT signin_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.signup
    ADD CONSTRAINT signup_pkey PRIMARY KEY (id);

-- Unique:

ALTER TABLE ONLY public.signup
    ADD CONSTRAINT unique_key UNIQUE (username);

ALTER TABLE ONLY public.signup
    ADD CONSTRAINT unique_email UNIQUE (email);

ALTER TABLE ONLY public.signup
    ADD CONSTRAINT unique_first_name UNIQUE (first_name);

ALTER TABLE ONLY public.signup
    ADD CONSTRAINT unique_last_name UNIQUE (last_name);

-- Foreign Key:

ALTER TABLE ONLY public.donation
    ADD CONSTRAINT fk_donator_id FOREIGN KEY (donator_id) REFERENCES public.user(user_id);

ALTER TABLE ONLY public.donation
    ADD CONSTRAINT fk_campaign_id FOREIGN KEY (campaign_id) REFERENCES public.campaign(campaign_id);

ALTER TABLE ONLY public.newsfeed
    ADD CONSTRAINT fk_newsfeed_donator_id FOREIGN KEY (author_id) REFERENCES public.user(user_id);

ALTER TABLE ONLY public.user
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES public.signin(id);
