CREATE DATABASE game_category

CREATE TABLE public.ms_game_title (
    id integer NOT NULL,
    game_title character varying NOT NULL,
    is_active smallint DEFAULT 1 NOT NULL,
    create_timestamp timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    update_timestamp timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE SEQUENCE public.ms_game_title_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.ms_game_title_id_seq OWNED BY public.ms_game_title.id;

ALTER TABLE ONLY public.ms_game_title ALTER COLUMN id SET DEFAULT nextval('public.ms_game_title_id_seq'::regclass);

INSERT INTO public.ms_game_title VALUES (1, 'Warhammer 40,000: Dawn of War', 1, '2025-01-01 22:35:04.540613', '2025-01-01 22:35:04.540613');
INSERT INTO public.ms_game_title VALUES (2, 'Forgive Me Father', 1, '2025-01-01 22:35:13.760134', '2025-01-01 22:35:13.760134');


SELECT pg_catalog.setval('public.ms_game_title_id_seq', 2, true);

ALTER TABLE ONLY public.ms_game_title
    ADD CONSTRAINT ms_game_title_pk PRIMARY KEY (id);

ALTER TABLE ONLY public.ms_game_title
    ADD CONSTRAINT ms_game_title_unique_1 UNIQUE (game_title);

CREATE OR REPLACE FUNCTION public.func_update_timestamp()
    RETURNS trigger
    LANGUAGE plpgsql
AS $function$
BEGIN
    NEW.update_timestamp = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$function$
;

CREATE TRIGGER trigger_ms_game_title_update_timestamp BEFORE UPDATE ON public.ms_game_title FOR EACH ROW EXECUTE FUNCTION public.func_update_timestamp();

